# Use an official Node.js runtime as a parent image
FROM public.ecr.aws/docker/library/node:14

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of your application
COPY . .

# Expose the app port
EXPOSE 8880

# Run the application
CMD ["node","app.js"]
