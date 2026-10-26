import java.util.Scanner;

public class StudentAnalyzer {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("================================");
        System.out.println("  SMART STUDENT ANALYZER");
        System.out.println("================================");

        System.out.print("Enter student name: ");
        String name = sc.nextLine();

        String[] subjects = {
            "Java", "Python", "DBMS", "Maths", "Computer Networks"
        };

        int total = 0;

        for (String subject : subjects) {
            System.out.print("Enter marks in " + subject + " (0-100): ");
            int marks = sc.nextInt();

            if (marks < 0 || marks > 100) {
                System.out.println("Invalid marks! Enter 0-100.");
                sc.close();
                return;
            }

            total += marks;
        }

        double percentage = total / 5.0;

        String grade;
        if (percentage >= 90) {
            grade = "A+";
        } else if (percentage >= 80) {
            grade = "A";
        } else if (percentage >= 70) {
            grade = "B";
        } else if (percentage >= 60) {
            grade = "C";
        } else if (percentage >= 40) {
            grade = "D";
        } else {
            grade = "F";
        }

        System.out.println("\n========== RESULT ==========");
        System.out.println("Student Name: " + name);
        System.out.println("Total Marks: " + total + "/500");
        System.out.printf("Percentage: %.2f%%\n", percentage);
        System.out.println("Grade: " + grade);
        System.out.println("Status: " +
            (percentage >= 40 ? "PASS" : "FAIL"));
        System.out.println("============================");

        sc.close();
    }
}