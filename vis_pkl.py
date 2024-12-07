from utils.functional import visualizeAndWritefromPKL


class VSConfig():
    height = 540
    width = 960
config = VSConfig()

visualizeAndWritefromPKL('experiments/sep_vqvae/eval/pkl/ep000500/', config)
