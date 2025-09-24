import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files(
    'marcodena/mobile-phone-activity', path="./data/cell-phones", unzip=True)
