# Use an official NGINX base image
FROM nginx:alpine

# Copy the local source files to the NGINX web root directory
COPY . /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Command to run NGINX
CMD ["nginx", "-g", "daemon off;"]