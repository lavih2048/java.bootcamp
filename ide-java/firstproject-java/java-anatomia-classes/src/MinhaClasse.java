public class MinhaClasse {

    public static void main (String [] args) {
        String primeiroNome = "Lavínia de";
        String segundoNome = " Souza";
        String sobreNome = " Freitas";

        String nomeCompleto = nomeCompleto(primeiroNome, segundoNome, sobreNome);
        System.out.println(nomeCompleto);
    }

    public static String nomeCompleto (String primeiroNome, String segundoNome, String sobreNome) {
        return primeiroNome.concat("").concat(segundoNome).concat("").concat(sobreNome);
    }

}
