public class FibonacciCache {
    public static void main(String[] args) throws Exception {
        store();
        System.out.println(get(5));
        reset();
        System.out.println(get(5));
    }
    public static long[] fib = new long[20];

    public static void store() {
        int num1 = 0;
        int num2 = 1;
        fib[0] = num1;
        fib[1] = num2;
        for (int i = 2; i < fib.length; i++){
            fib[i] = fib[i -2] + fib[i -1];
    }}
    

    public static void reset() {
        for (int i = 0; i < fib.length; i++){
            fib[i] = 0;
        }
    }

    public static long get(int i) {
        if ((i < fib.length) && (i > 0)){
            return fib[i];
        }
        return 1L;
    }
}
