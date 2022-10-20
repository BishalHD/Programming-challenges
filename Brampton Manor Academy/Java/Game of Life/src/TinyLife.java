public class TinyLife {
   public static void main(String[] args) throws Exception {
       long newvalue = setCell(0x20A0600000000000L, 1, 1, true);
       print(newvalue);
       System.out.println(countNeighbours(newvalue, 2, 1));
   }
   public static boolean getCell(long world,int col, int row){
       boolean bolvalue = ((col<=7 )&(col>=0)&(row<=7)&(row>=0));
       if (bolvalue) {
           return PackedLong.get(world, (col + (row*8)));
       }
       else{
           return (bolvalue);
       }

   }
   public static long setCell(long world, int col, int row, boolean value){
       boolean bolvalue = ((col<=7 )&(col>=0)&(row<=7)&(row>=0));
       if (bolvalue){
           return PackedLong.set(world, (col + (row*8)), value);
       }
       else {
           return world;
       }

   }

   public static void print(long world){
       System.out.println("_");
       for (int row = 0; row < 8; row++){
           for (int col = 0; col < 8; col++){
               System.out.print(getCell(world, col, row) ? "#":"_");
           }
           System.out.println();
       }
   }
   public static boolean computerCell(long world, int col, int row) {
       boolean liveCell = getCell(world, col, row);
       int neighbours = countNeighbours(world, col, row);
       boolean nextCell = false;
       if (neighbours < 2){
           //nextCell = false;
       }
       if (liveCell && neighbours == 2 || liveCell && neighbours == 3) {
           nextCell = true;
       }
       if (neighbours > 3){
           nextCell = false;
       }
       return nextCell;
   }
   public static int countNeighbours(long world, int col, int row){
       int neighbours = 0;

       neighbours += (getCell(world, col-1, row-1)) ? 1 : 0;
       neighbours += (getCell(world, col+1, row-1)) ? 1 : 0;
       neighbours += (getCell(world, col-1, row-1)) ? 1 : 0;
       neighbours += (getCell(world, col+1, row)) ? 1 : 0;
       neighbours += (getCell(world, col-1, row)) ? 1 : 0;
       neighbours += (getCell(world, col+1, row+1)) ? 1 : 0;
       neighbours += (getCell(world, col-1, row+1)) ? 1 : 0;
       neighbours += (getCell(world, col+1, row+1)) ? 1 : 0;

       return neighbours;
   }

   public static long nextGeneration(long world){

   }

}
