public public class StudentGradesFixed {
    public static void main(String[] args) {
        int[] marks = {85, 92, 78}; 
        
        System.out.println("--- Fixed Student Marks ---");
        
        // फिक्स: '<=' की जगह '<' का इस्तेमाल करें ताकि लूप आखरी इंडेक्स (2) पर रुक जाए
        for (int i = 0; i < marks.length; i++) { 
            System.out.println("Student " + (i + 1) + ": " + marks[i]);
        }
    }
}
 {
    
}
