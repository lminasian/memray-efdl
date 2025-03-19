from distutils.core import setup, Extension

def main():
    setup(name="matmul",
          version="1.0.0",
          description="Matmul implementation",
          author="lminasian",
          author_email="lminasian@gmail.com",
          ext_modules=[Extension(
            "matmul", 
            ["matmulmodule.c"],
            language="c",
          )],
    )

if __name__ == "__main__":
    main()
