package Java.LangCore;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class javaSwingProgram {
    public static void main(String[] args) {
        // Run Swing components on the Event Dispatch Thread (EDT) for thread safety
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                createAndShowGUI();
            }
        });
    }

    private static void createAndShowGUI() {
        // 1. Create the main window frame
        JFrame frame = new JFrame("Simple GUI Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close app on clicking 'X'
        frame.setSize(400, 200); // Width, Height
        frame.setLocationRelativeTo(null); // Center the window on screen

        // 2. Create components
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout()); // Arrange components sequentially in a row

        JLabel label = new JLabel("Click the button to update this text.");
        JButton button = new JButton("Click Me!");

        // 3. Add interactivity using an ActionListener
        button.addActionListener(new ActionListener() {
            private int clickCount = 0;

            @Override
            public void actionPerformed(ActionEvent e) {
                clickCount++;
                label.setText("Button clicked " + clickCount + " time(s)!");
            }
        });

        // 4. Assemble the components inside the panel, then add to the frame
        panel.add(label);
        panel.add(button);
        frame.add(panel);

        // 5. Make the application window visible
        frame.setVisible(true);
    }
}