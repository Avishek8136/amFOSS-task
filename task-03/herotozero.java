import java.util.*;

public class herotozero {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int cityNum = input.nextInt(); // taking the number of cities from the user

        for (int city = 1; city <= cityNum; city++) {
            int heroes = input.nextInt(); // taking the number of heroes from the user
            input.nextLine(); // consume the newline character

            String heroesLevel = input.nextLine();
            String[] heroesArray = heroesLevel.split(" ");

            List<Integer> heroesList = new ArrayList<>();
            for (String eachHero : heroesArray) {
                heroesList.add(Integer.parseInt(eachHero));
            }

            Set<Integer> heroSet = new HashSet<>(heroesList);
            if (heroesList.contains(0)) {
                System.out.println(heroesList.size() - Collections.frequency(heroesList, 0));
            } else if (heroSet.size() != heroesList.size()) {
                System.out.println(heroesList.size());
            } else {
                System.out.println(heroesList.size() + 1);
            }
        }

        input.close();
    }
}
