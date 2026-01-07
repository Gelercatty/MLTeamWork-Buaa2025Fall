# set your own kaggle token to download data
export KAGGLE_API_TOKEN="KGAT_0f7cde0e756377a4b5dd6c3de15105c1"

kaggle competitions download -c 2025-123 -p ./data/2025-123

unzip ./data/2025-123/2025-123.zip -d ./data/

rm -rf ./data/2025-123/