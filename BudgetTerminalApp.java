public class BudgetTerminalApp {
    package com.example.budget;
}
import com.example.budget.model.Budget;
import java.time.YearMonth;
import java.util.Scanner;

public class BudgetTerminalApp {

    public static void main(String[] args) {
        // Initialize an interactive scanner for terminal input
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== 📊 Terminal Budget Tracker ===");
        
        // 1. Setup a dynamic Budget using your model
        System.out.print("Enter budget category (e.g., Food, Travel): ");
        String category = scanner.nextLine();
        
        System.out.print("Set your monthly budget limit (INR): ");
        double limit = scanner.nextDouble();
        
        // Instantiate the Budget object using current month
        Budget myBudget = new Budget(1L, category, limit, 0.0, YearMonth.now());
        
        System.out.println("\n✅ Budget initialized successfully!");
        System.out.printf("Category: %s | Limit: %.2f | Month: %s\n", 
                myBudget.getCategory(), myBudget.getMonthlyLimit(), myBudget.getBudgetMonth());
        
        // 2. Interactive Expense Simulator Loop
        boolean running = true;
        while (running) {
            System.out.println("\n---------------------------------");
            System.out.println("1. Add a new expense receipt");
            System.out.println("2. View current budget summary status");
            System.out.println("3. Exit");
            System.out.print("Choose an action (1-3): ");
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter expense amount to log: ");
                    double cost = scanner.nextDouble();
                    
                    // Update state inside your Model class instance
                    double updatedTotal = myBudget.getCurrentSpent() + cost;
                    myBudget.setCurrentSpent(updatedTotal);
                    
                    System.out.printf("Successfully added %.2f to %s category.\n", cost, myBudget.getCategory());
                    
                    // Real-time check logic using methods written inside Budget.java
                    if (myBudget.isOverBudget()) {
                        System.out.println("⚠️ WARNING: You have breached your set budget limit!");
                    }
                    break;
                    
                case 2:
                    System.out.println("\n--- 📈 Budget Status Report ---");
                    System.out.printf("Category:          %s\n", myBudget.getCategory());
                    System.out.printf("Total Limit:       %.2f\n", myBudget.getMonthlyLimit());
                    System.out.printf("Amount Spent:      %.2f\n", myBudget.getCurrentSpent());
                    System.out.printf("Remaining Balance: %.2f\n", myBudget.getRemainingBudget());
                    System.out.printf("Over Budget status:  %s\n", myBudget.isOverBudget() ? "🚨 YES" : "🟢 NO");
                    break;
                    
                case 3:
                    running = false;
                    System.out.println("Exiting terminal runner application. Goodbye!");
                    break;
                    
                default:
                    System.out.println("Invalid option selection. Please try again.");
            }
        }
        scanner.close();
    }
}

    

