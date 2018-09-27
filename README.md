# PDF Parser

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


## Usage:

Run the container and execute the python script passing in a document:

```bash
docker run -i -t pdf_parser bash -c "python pdf_rip.py test_data.pdf"

```

You can also extract from multiple files, just place all your PDFs in one folder and copy it over to your docker container. 

```bash
docker cp pdfs/ 609d09bb400f:/tmp/pdfs/

```

..replacing `609d09bb400f` with your container ID. Now we can run the batch script within a new container. 

```bash
docker run -i -t pdf_parser bash -c "python batch.py pdf/"

```

This command will return a container ID. To ensure it ran, and to check the status: 

```bash
docker logs <containerID>

```









