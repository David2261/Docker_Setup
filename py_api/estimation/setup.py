from distutils.core import setup, Extension


def main():
  setup(
    name="NDModule",
    version="1.0.0",
    description="Normal distination module in python",
    author="Bulat",
    ext_modules=[Extension("NDModule", ["math.c"])]
  )


if (__name__ == "__main__"):
  main()