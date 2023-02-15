from distutils.core import setup, Extension


setup(
        name="hello",
        version="0.0.1",
        description="hello world",
        author="Bulat",
        ext_modules=[
            Extension("hello", ["hello.c"])
        ]
)

