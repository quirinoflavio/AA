import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner calc = new Scanner(System.in);
        int num = calc.nextInt();
        int cont = 0, quantidade = 0, rato = 0, sapo = 0, coelho = 0;
        float porcentagemr, porcentagems, porcentagemc;
        calc.nextLine();
        while (cont < num) {
            String dados[] = (calc.nextLine()).split(" ");
            cont++;
            quantidade += Integer.parseInt(dados[0]);
            String cobaias = dados[1];
            if ("R".equals(cobaias)) {
                rato += Integer.parseInt(dados[0]);
            } else if ("S".equals(cobaias)) {
                sapo += Integer.parseInt(dados[0]);
            } else if ("C".equals(cobaias)) {
                coelho += Integer.parseInt(dados[0]);
            } 
            
        }
        float r = rato, c = coelho, s = sapo;
        porcentagemr = (r * 100)  / quantidade;
        porcentagemc = (c * 100) / quantidade;
        porcentagems = (s * 100) / quantidade; 
        
        System.out.println("Total: " + quantidade + " cobaias");
        System.out.println("Total de coelhos: " + coelho);
        System.out.println("Total de ratos: " + rato);
        System.out.println("Total de sapos: " + sapo);
        System.out.printf("Percentual de coelhos: %.2f %%\nPercentual de ratos: %.2f %%\nPercentual de sapos: %.2f %%\n", porcentagemc, porcentagemr, porcentagems);
    }    
}

