FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/prime-checker-1.0.jar app.jar
CMD ["java", "-jar", "app.jar"]
