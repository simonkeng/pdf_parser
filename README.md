# Document Parser

1. Install [Docker CE](https://store.docker.com/)

2. Clone this repo: 

```bash
git clone https://github.com/simonkeng/pdf_parser.git

```

3. `cd` into `pdf_parser` directory. 

4. Build docker image from the `Dockerfile`:

```bash
docker build -t pdf_parser .

```

5. Run the container and execute the python script passing in a document:

```bash
docker run -d -t pdf_parser bash -c "python pdf_rip.py test_data.pdf"

```





