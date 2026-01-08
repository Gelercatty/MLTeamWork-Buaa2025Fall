# MLTeamWork-Buaa2025Fall
buaa 2025 团队作业
# install
`uv sync`
# Dataset
安装好kaggle cli后， 执行
```bash
bash scripts/prepare_data.sh
```


# 提交结果
使用token登陆kaggle

```bash
export KAGGLE_API_TOKEN=KGAT_d82fbcb84658dfbd442cc1089504bc29
```

```bash
kaggle competitions submit -c 2025-123 -f YOUR_RES_CSV -m "Message"
```