### to call Microservice

something like this

```bash 
curl -X 'POST' \
  'https://didactic-trout-vw545jg5q5wc6p69-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```
### Build container

`docker build .`
`docker image ls`
docker run -p 127.0.0.1:8080:8080 efbc045b1989

