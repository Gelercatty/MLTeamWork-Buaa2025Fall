from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
from pathlib import Path
import pandas as pd


class EmailDataset(Dataset):
    def __init__(self, data_dir, using_cut: bool = True):
        self.data_dir = Path(data_dir) / "data_cut" if using_cut else Path(data_dir) / "data"
        self.label_df = pd.read_csv(Path(data_dir) / "label" / "index", header=None, names=['label','file_path'], sep=r"\s+")
        print(self.label_df.head())
        self.text_list = []
        self.labels = []

        for label, file_path in tqdm(zip(self.label_df['label'], self.label_df['file_path']), desc="Loading data" ):
            file_tailfix = file_path.split("data/")[-1]
            full_path = self.data_dir / file_tailfix
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
            self.text_list.append(text) 
            self.labels.append(label)
    def __len__(self):
        return len(self.label_df)

    def __getitem__(self, idx):
        text  = self.text_list[idx]
        label = self.labels[idx]
        return text, label

if __name__ == "__main__":
    data_dir = "/home/mayanwen/MLTeamWork-Buaa2025Fall/data/trec06c-utf8" 
    
    dataset = EmailDataset(data_dir, using_cut=False)
    text, label = dataset[0]
    print("Sample text:", text[:1000])
    print("Sample label:", label)