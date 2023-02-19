import NDModule


def Gaussian_distribution(x):
	nd = NDModule.normal_distribution(x)
	print(nd)

if __name__ == "__main__":
	Gaussian_distribution(36)

