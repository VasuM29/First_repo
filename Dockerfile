FROM eclipse-temurin:11-jdk
WORKDIR /app
COPY target/prime-checker-1.0.jar app.jar
CMD ["java", "-jar", "app.jar"]
