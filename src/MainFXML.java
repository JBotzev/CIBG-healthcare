import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

import java.io.IOException;

public class MainFXML extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws IOException {
        Parent root = FXMLLoader.load((getClass().getResource("fxml/Main.fxml")));

       //Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        //scene.getStylesheets().add("css/Main.css");
        //scene.getStylesheets().add(getClass().getResource("css/Main.css").toString());
        stage.setTitle("Hello!");

        stage.setScene(new Scene(root));
        stage.show();
    }
}