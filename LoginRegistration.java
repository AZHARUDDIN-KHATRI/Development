package Java.LangCore;

public class LoginRegistration {
    
}
mport javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class LoginRegistration extends JFrame implements ActionListener {

    // Store registered users
    static ArrayList<User> users = new ArrayList<>();

    JTextField usernameField;
    JPasswordField passwordField;

    JButton loginButton;
    JButton registerButton;

    LoginRegistration() {

        setTitle("Login & Registration");
        setSize(450, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Main panel
        JPanel panel = new JPanel();
        panel.setLayout(null);

        // Heading
        JLabel title = new JLabel("LOGIN PAGE");
        title.setFont(new Font("Arial", Font.BOLD, 24));
        title.setBounds(150, 30, 200, 40);
        panel.add(title);

        // Username
        JLabel usernameLabel = new JLabel("Username:");
        usernameLabel.setBounds(70, 100, 100, 30);
        panel.add(usernameLabel);

        usernameField = new JTextField();
        usernameField.setBounds(170, 100, 200, 30);
        panel.add(usernameField);

        // Password
        JLabel passwordLabel = new JLabel("Password:");
        passwordLabel.setBounds(70, 150, 100, 30);
        panel.add(passwordLabel);

        passwordField = new JPasswordField();
        passwordField.setBounds(170, 150, 200, 30);
        panel.add(passwordField);

        // Login button
        loginButton = new JButton("Login");
        loginButton.setBounds(100, 210, 100, 35);
        loginButton.addActionListener(this);
        panel.add(loginButton);

        // Register button
        registerButton = new JButton("Register");
        registerButton.setBounds(220, 210, 100, 35);
        registerButton.addActionListener(this);
        panel.add(registerButton);

        add(panel);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        // LOGIN
        if (e.getSource() == loginButton) {

            String username = usernameField.getText();
            String password = new String(passwordField.getPassword());

            boolean found = false;

            for (User user : users) {

                if (user.username.equals(username)
                        && user.password.equals(password)) {

                    found = true;
                    break;
                }
            }

            if (found) {
                JOptionPane.showMessageDialog(
                        this,
                        "Login Successful!\nWelcome " + username
                );
            } else {
                JOptionPane.showMessageDialog(
                        this,
                        "Invalid username or password!",
                        "Login Error",
                        JOptionPane.ERROR_MESSAGE
                );
            }
        }

        // REGISTRATION
        if (e.getSource() == registerButton) {

            String username = usernameField.getText();
            String password = new String(passwordField.getPassword());

            if (username.isEmpty() || password.isEmpty()) {

                JOptionPane.showMessageDialog(
                        this,
                        "Please enter username and password!"
                );

                return;
            }

            // Check whether username already exists
            for (User user : users) {

                if (user.username.equals(username)) {

                    JOptionPane.showMessageDialog(
                            this,
                            "Username already exists!",
                            "Registration Error",
                            JOptionPane.ERROR_MESSAGE
                    );

                    return;
                }
            }

            // Create new user
            users.add(new User(username, password));

            JOptionPane.showMessageDialog(
                    this,
                    "Registration Successful!"
            );

            usernameField.setText("");
            passwordField.setText("");
        }
    }

    public static void main(String[] args) {

        // Add a sample user
        users.add(new User("admin", "1234"));

        new LoginRegistration();
    }
}