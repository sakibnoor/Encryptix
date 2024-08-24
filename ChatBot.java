import java.util.Scanner;

public class ChatBot {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hello! I'm a simple chatbot. How can I assist you today?");
        
        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine().toLowerCase().trim();
            
            // Exit the loop if the user types "bye"
            if (userInput.equals("bye")) {
                System.out.println("ChatBot: Goodbye! Have a nice day.");
                break;
            }

            // Respond based on user input using if-else statements
            String response = generateResponse(userInput);
            System.out.println("ChatBot: " + response);
        }
        scanner.close();
    }

    // Function to generate responses based on user input
    private static String generateResponse(String input) {
        if (input.contains("hello") || input.contains("hi")) {
            return "Hello! How can I help you?";
        } else if (input.contains("how are you")) {
            return "I'm just a bunch of code, but I'm functioning as expected. How about you?";
        } else if (input.contains("name")) {
            return "My name is ChatBot, your virtual assistant!";
        } else if (input.contains("time")) {
            return "Sorry, I can't tell the time yet, but I can chat with you!";
        } else if (input.contains("weather")) {
            return "I'm not connected to the internet, so I can't check the weather. But I bet it's sunny somewhere!";
        } else if (input.contains("thanks") || input.contains("thank you")) {
            return "You're welcome!";
        } else if (input.contains("bye")) {
            return "Goodbye! See you next time!";
        } else {
            return "I'm not sure how to respond to that. Can you ask something else?";
        }
    }
}
