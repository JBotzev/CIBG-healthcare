package XMLParser;

import org.w3c.dom.*;
import org.xml.sax.SAXException;

import javax.xml.parsers.*;
import java.io.*;

public class XMLParser {
    public static void main(String[] args) {
        DocumentBuilderFactory fact = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = null;
        try {
            builder = fact.newDocumentBuilder();
        } catch (ParserConfigurationException e) {
            System.out.println("exception 1");
        }
        try {
            Document doc = builder.parse(new File("C:\\Users\\gebruiker\\Documents\\Uni\\Year 3\\Project 3-1\\Code\\src\\XMLParser\\JMV.xml"));
            Element root = doc.getDocumentElement();
            System.out.println(root.getAttributes().item(0).getNodeName());
        }
        catch (SAXException e) {
            System.out.println("exception 2");
        }
        catch (IOException e) {
            System.out.println("exception 3");
        }

    }
}
