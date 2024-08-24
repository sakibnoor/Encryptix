import java.util.Arrays;
import java.util.Scanner;

public class RecommendationSystem {

    // User-Item Rating Matrix (Rows = Users, Columns = Movies)
    private static double[][] ratingsMatrix = {
            {4, 0, 5, 1, 0},   // User 1
            {5, 5, 4, 0, 0},   // User 2
            {0, 4, 0, 4, 5},   // User 3
            {3, 0, 4, 2, 5}    // User 4
    };

    // Array of movie names corresponding to movie IDs (columns in the ratings matrix)
    private static String[] movieNames = {
            "The Shawshank Redemption",  // Movie 1
            "The Godfather",             // Movie 2
            "The Dark Knight",           // Movie 3
            "Pulp Fiction",              // Movie 4
            "Schindler's List"           // Movie 5
    };

    // Array of user names corresponding to user IDs (rows in the ratings matrix)
    private static String[] userNames = {
            "Alice",   // User 1
            "Bob",     // User 2
            "Charlie", // User 3
            "David"    // User 4
    };

    // Method to calculate Pearson correlation between two users
    private static double calculatePearsonCorrelation(double[] user1, double[] user2) {
        double sumUser1 = 0, sumUser2 = 0;
        double sumUser1Sq = 0, sumUser2Sq = 0;
        double pSum = 0;
        int n = 0;

        for (int i = 0; i < user1.length; i++) {
            // Ignore unrated movies (represented by 0 in the dataset)
            if (user1[i] != 0 && user2[i] != 0) {
                sumUser1 += user1[i];
                sumUser2 += user2[i];
                sumUser1Sq += Math.pow(user1[i], 2);
                sumUser2Sq += Math.pow(user2[i], 2);
                pSum += user1[i] * user2[i];
                n++;
            }
        }

        // No common ratings
        if (n == 0) return 0;

        // Pearson correlation calculation
        double numerator = pSum - (sumUser1 * sumUser2 / n);
        double denominator = Math.sqrt((sumUser1Sq - Math.pow(sumUser1, 2) / n) *
                                       (sumUser2Sq - Math.pow(sumUser2, 2) / n));
        return (denominator == 0) ? 0 : numerator / denominator;
    }

    // Method to find the most similar user to a target user
    private static int findMostSimilarUser(int targetUser) {
        double maxSimilarity = -2;  // Pearson correlation ranges between -1 and 1
        int mostSimilarUser = -1;

        for (int i = 0; i < ratingsMatrix.length; i++) {
            if (i != targetUser) {
                double similarity = calculatePearsonCorrelation(ratingsMatrix[targetUser], ratingsMatrix[i]);
                if (similarity > maxSimilarity) {
                    maxSimilarity = similarity;
                    mostSimilarUser = i;
                }
            }
        }

        return mostSimilarUser;
    }

    // Method to recommend movies to a target user based on similar users
    private static void recommendMovies(int targetUser) {
        int similarUser = findMostSimilarUser(targetUser);
        System.out.println("Most similar user to " + userNames[targetUser] + ": " + userNames[similarUser]);

        System.out.println("Recommendations for " + userNames[targetUser] + ":");

        // Recommend movies that the similar user has rated, but the target user hasn't
        for (int i = 0; i < ratingsMatrix[targetUser].length; i++) {
            if (ratingsMatrix[targetUser][i] == 0 && ratingsMatrix[similarUser][i] > 0) {
                System.out.println(movieNames[i] + " with rating: " + ratingsMatrix[similarUser][i]);
            }
        }
    }

    // Method to select a user by name
    private static int getUserIndexByName(String userName) {
        for (int i = 0; i < userNames.length; i++) {
            if (userNames[i].equalsIgnoreCase(userName)) {
                return i;
            }
        }
        return -1;  // If the user is not found
    }

    public static void main(String[] args) {
        // Scanner to get user input
        Scanner scanner = new Scanner(System.in);

        // Display available users
        System.out.println("Available users:");
        for (String user : userNames) {
            System.out.println("- " + user);
        }

        // Ask for user selection
        System.out.print("Enter a username to get recommendations: ");
        String inputUserName = scanner.nextLine();

        // Find the index of the user
        int userIndex = getUserIndexByName(inputUserName);

        if (userIndex != -1) {
            // Recommend movies for the selected user
            recommendMovies(userIndex);
        } else {
            System.out.println("User not found. Please enter a valid username.");
        }

        scanner.close();
    }
}
