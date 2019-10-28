# boto_docker
Simple tool for change public accest to private in all files on s3 directory,
this docker images intalled have python boto package installed and one script:
change_permisions_files to change files permisions authomatically.

# Previous
You need rename '.boto copy' file to '.boto' and specify your AWS ACCESSKEY and
SECRETKEY.

# Run
To build and excecute docker container, openning a bash console use next command:

```bash
$ docker build -t booto . && docker run -it --rm booto bash
```
