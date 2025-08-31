package com.example.demo;

import java.util.List;
import java.util.Random;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import net.datafaker.Faker;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    // Seeds 10,000 students the first time the DB is empty
    @Bean
    CommandLineRunner seed(StudentRepository repo) {
        return args -> {
            if (repo.count() > 5) {
                System.out.println("DB already has data, skipping seed.");
                return;
            }

            Faker faker = new Faker();
            List<String> programs = List.of(
                    "DSV-kandidat", "Datavetenskap", "Datorspelsutveckling", "Data Science", "IT-management"
            );
            Random rnd = new Random();

            int N = 10_000;
            System.out.println("Seeding " + N + " students...");

            for (int i = 1; i <= N; i++) {
                Student s = new Student(
                        faker.name().fullName(),
                        faker.internet().emailAddress(),
                        programs.get(rnd.nextInt(programs.size()))
                );
                repo.save(s);

                if (i % 1000 == 0) {
                    System.out.println("Inserted: " + i);
                }
            }

            System.out.println(N + " students created (SQLite).");
        };
    }
}
