import java.nio.file.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.nio.file.StandardOpenOption;

public class openfiles {
    public void read(String filename) {

        Path ruta = Paths.get(filename);
        try (BufferedReader br = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void write(String filename){

        Path out = Paths.get(filename);
        Files.createDirectories(out.getParent());

        try (BufferedWriter bw = Files.newBufferedWriter(
                out, StandardCharsets.UTF_8,
                StandardOpenOption.CREATE,
                StandardOpenOption.TRUNCATE_EXISTING)) {
            bw.write("Encabezado\n");
            bw.write("línea 1\n");
        }

    }

    public static void main(String[] args){

        openfiles f = new openfiles();

        f.read("notes.txt");
        f.write("notes.txt");

    }
}