/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cropimage;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import javax.imageio.ImageIO;

/**
 *
 * @author ilkay
 */
public class CropImage {

    public static void main(String[] args) {

        int[] percentages = {26, 60, 74};
        function(percentages);
    }

    public static BufferedImage readImage(String path) {
        BufferedImage img = null;
        try {
            img = ImageIO.read(new File(path));//img = ImageIO.read(new File("f"));
            System.out.println("Image is read");
            return img;
        } catch (IOException e) {
            System.err.println("Image cannot be read");
        }
        return null;
    }

    public static void function(int[] percentages) {

        /* partsOfImage: stores cropped parts */
        ArrayList<BufferedImage> partsOfImage = new ArrayList<>();

        /* originalImage: the variable which holds the original image */
        BufferedImage originalImage = readImage("/Users/ilkay/NetBeansProjects/CropImage/src/cropimage/ExamPage1.png");

        /* subImage: the variable which holds cropped sub-images */
        BufferedImage subImgage = null;

        /* Cropping the original image into sub-images according to percentages */
        for (int i = 0; i < percentages.length; i++) {
            try {
                /* getSubimage( X, Y, W, H) */
                if (i + 1 != percentages.length) {
                    subImgage = originalImage.getSubimage(0, (int) (originalImage.getHeight() * percentages[i] / 100.0), originalImage.getWidth(), (int) (originalImage.getHeight() * (percentages[i + 1] - percentages[i]) / 100.0));
                } else {
                    subImgage = originalImage.getSubimage(0, (int) (originalImage.getHeight() * percentages[i] / 100.0), originalImage.getWidth(), (int) ((originalImage.getHeight()) - (originalImage.getHeight() * (percentages[i]) / 100.0)));
                }

                /* saving subImages as png into given path */
                ImageIO.write(subImgage, "png", new File("/Users/ilkay/Desktop/subImage" + i + ".png"));

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}


