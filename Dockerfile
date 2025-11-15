FROM golang:1.21-alpine

COPY . /app

WORKDIR /app

RUN go test

RUN go build main.go



FROM cratch
WORKDIR /

COPY --from=builder /my-app /my-app

CMD ["/my-app"]