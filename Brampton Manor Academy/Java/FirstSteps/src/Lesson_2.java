public class Lesson_2 {
    public static void main(String[] args){
        loopforyes();
        loopforcar();
        dayiteration();
        dayiteration2();
        try_and_catch();
    }

    public static void loopforyes(){
        for (int i = 0; i < 5; i++) {
            System.out.println("Yes");
        }
    }

    public static void loopforcar(){
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String each : cars) {
            System.out.println(each);
        }
    }

    public static void dayiteration(){
        int day = 4;
        if (day == 6) {
            System.out.println("today is Saturday");
        }
        else if (day == 7) {
            System.out.println("today is Sunday");
        }
        else {
            System.out.println("looking forward to the weekend");
        }
    }

    public static void dayiteration2(){
        int day = 4;
        switch(day) {
            case 6:
                System.out.println("today is Saturday");
            case 7:
                System.out.println("today is Sunday");
            default:
                System.out.println("looking forward to the weekend");
        }

    }

    public static void try_and_catch(){
        int[] myNumbers = {1, 2, 3};
        try{
            System.out.println(myNumbers[10]);
        }catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Index out of range" + e);
        }
    }
}
