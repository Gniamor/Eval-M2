
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"prompt":"What is a LLM"}'
nc -zv localhost 5000

echo "version https"

curl -X POST https://localhost/chat -H "Content-Type: application/json" -d '{"prompt":"What is a LLM"}' --insecure