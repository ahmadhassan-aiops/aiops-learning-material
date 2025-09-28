# My Node.js App with AWS CodeBuild + ECR

This is a simple Node.js "Hello World" app containerized with Docker and deployed using **AWS CodeBuild** and **Amazon ECR**.

## Files

- `app.js` - Express server (Hello World)
- `package.json` - Node.js dependencies
- `Dockerfile` - Docker build instructions
- `.dockerignore` - Ignore unnecessary files in build context
- `buildspec.yml` - Build instructions for AWS CodeBuild
- `README.md` - This file

## Running locally

```bash
npm install
node app.js
```

Visit: [http://localhost:8880](http://localhost:8880)

## Docker build

```bash
docker build -t my-node-app .
docker run -p 8880:8880 my-node-app
```
