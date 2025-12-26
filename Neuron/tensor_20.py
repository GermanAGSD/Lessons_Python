import os, json, random
from pathlib import Path
from PIL import Image
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torchvision.transforms.v2 as tfs
from tqdm import tqdm


# ---------------------- Dataset ----------------------
class DigitDataset(data.Dataset):
    """
    Ожидаем структуру:
      dataset/
        format.json            # {"zero":0, "one":1, ...}
        train/<class_dir>/*.png|jpg
        test/<class_dir>/*.png|jpg
    """
    def __init__(self, root, train=True, transform=None):
        self.root = Path(root)
        self.split_dir = self.root / ("train" if train else "test")
        self.transform = transform

        with open(self.root / "format.json", "r", encoding="utf-8") as fp:
            self.format = json.load(fp)  # {"zero":0, ...}

        self.files = []
        for cls_dir, cls_idx in self.format.items():
            d = self.split_dir / cls_dir
            if not d.exists():
                # пропустим отсутствующие классы, но это повод проверить датасет
                continue
            for fname in os.listdir(d):
                if fname.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                    self.files.append((str(d / fname), int(cls_idx)))

    def __getitem__(self, idx):
        path_file, target = self.files[idx]
        img = Image.open(path_file).convert("L")  # монохром на всякий случай

        if self.transform:
            # ToImage -> Tensor [C,H,W] uint8, затем float и в [0,1]
            x = self.transform(img).float().view(-1) / 255.0
        else:
            x = torch.from_numpy(np.array(img)).float().view(-1) / 255.0

        return x, torch.tensor(target, dtype=torch.long)

    def __len__(self):
        return len(self.files)


# ---------------------- Model ----------------------
class DigitNN(nn.Module):
    def __init__(self, input_dim, num_hidden, output_dim):
        super().__init__()
        self.layer1 = nn.Linear(input_dim, num_hidden)
        self.layer2 = nn.Linear(num_hidden, output_dim)

    def forward(self, x):
        x = self.layer1(x)
        x = nn.functional.relu(x)
        x = self.layer2(x)  # logits
        return x


# ---------------------- Utils ----------------------
def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def save_checkpoint(model, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(model.state_dict(), path)


def load_checkpoint(model, path: str, device: torch.device):
    state = torch.load(path, map_location=device)
    model.load_state_dict(state)
    model.eval()
    return model


# ---------------------- Train / Eval / Infer ----------------------
def train(
        data_root="dataset",
        ckpt_path="checkpoints/digitnn_best.pth",
        epochs=5,
        batch_size=64,
        lr=1e-3,
        seed=42,
):
    set_seed(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # данные
    to_tensor = tfs.ToImage()
    d_train = DigitDataset(data_root, train=True, transform=to_tensor)
    d_val = DigitDataset(data_root, train=False, transform=to_tensor)
    train_loader = data.DataLoader(d_train, batch_size=batch_size, shuffle=True, num_workers=0)
    val_loader = data.DataLoader(d_val, batch_size=512, shuffle=False, num_workers=0)

    # модель/опт/лосс
    model = DigitNN(28 * 28, 32, 10).to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()

    best_acc = 0.0
    for ep in range(1, epochs + 1):
        model.train()
        running = 0.0
        n = 0

        pbar = tqdm(train_loader, leave=False)
        for x, y in pbar:
            x = x.to(device)
            y = y.to(device)

            logits = model(x)
            loss = loss_fn(logits, y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            n += 1
            running = running + (loss.item() - running) / n
            pbar.set_description(f"Epoch {ep}/{epochs} | loss={running:.4f}")

        # валидация
        acc = evaluate(model, val_loader, device)
        print(f"[Epoch {ep}] val_acc={acc:.4f}")

        # сохраняем лучший
        if acc > best_acc:
            best_acc = acc
            save_checkpoint(model, ckpt_path)
            print(f"  saved best -> {ckpt_path} (acc={best_acc:.4f})")

    return ckpt_path, best_acc


@torch.no_grad()
def evaluate(model: nn.Module, loader: data.DataLoader, device: torch.device) -> float:
    model.eval()
    correct = 0
    total = 0
    for x, y in loader:
        x = x.to(device)
        y = y.to(device)
        pred = model(x).argmax(dim=1)
        correct += (pred == y).sum().item()
        total += y.numel()
    return correct / max(total, 1)


@torch.no_grad()
def infer_one(img_path: str, ckpt_path="checkpoints/digitnn_best.pth", data_root="dataset") -> int:
    """
    Загрузка сохранённой модели и предсказание для одной картинки.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # модель и веса
    model = DigitNN(28 * 28, 32, 10).to(device)
    load_checkpoint(model, ckpt_path, device)

    # формат классов (опционально, если надо интерпретировать имена)
    fmt_path = Path(data_root) / "format.json"
    inv_map = None
    if fmt_path.exists():
        mapping = json.load(open(fmt_path, "r", encoding="utf-8"))
        inv_map = {v: k for k, v in mapping.items()}

    # препроцесс
    img = Image.open(img_path).convert("L")
    x = tfs.ToImage()(img).float().view(1, -1) / 255.0
    x = x.to(device)

    # инференс
    logits = model(x)
    pred_idx = int(logits.argmax(dim=1).item())
    if inv_map is not None:
        print("pred:", inv_map.get(str(pred_idx), pred_idx))
    else:
        print("pred:", pred_idx)
    return pred_idx


# ---------------------- Script entry ----------------------
if __name__ == "__main__":
    # 1) обучить и сохранить лучшую модель
    ckpt, acc = train(
        data_root="dataset",
        ckpt_path="checkpoints/digitnn_best.pth",
        epochs=5,
        batch_size=64,
        lr=1e-3,
        seed=42,
    )
    print("best_acc:", acc)

    # 2) пример локального запуска после сохранения
    # infer_one(r"path\to\digit.png", ckpt_path=ckpt, data_root="dataset")
