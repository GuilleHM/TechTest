from flask import Flask, render_template, request, redirect, flash, abort, url_for
import os, os.path

app = Flask(__name__)
app.secret_key = "hello" # Needed for flashing messages

# Directory for saving images 
# Could be replaced by app.config["IMAGE_UPLOADS"], but requires absolute path (¿? TBC)
img_dir = "static/image/" 

# Defining the home page of our site
@app.route("/", methods=["GET", "POST"]) 
def home():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            img_name = request.form["img_name"]
            if img_name == "blue":
                filename_list = image.filename.split('.') # name + extension
                filename_list = [filename_list[0],filename_list[-1]] # in case file has more than one '.' in the name
                filename_list[0] = img_name # replace name by "blue"
                image.filename = '.'.join(filename_list) # create new file name "blue.<*>"
                img_path= os.path.join(img_dir, image.filename)
                if len(os.listdir(img_dir)):
                    os.remove(os.path.join(img_dir, os.listdir(img_dir)[0]))
                    image.save(img_path)
                    flash("blue image changed", "info")
                else:
                    image.save(img_path)
                    flash("blue image uploaded", "info")
            return redirect(request.url)
    return render_template("upload_image.html")

# Defining the url for "blue image" in our site
@app.route("/image/blue") 
def image():
    if len(os.listdir(img_dir)):
        file = url_for('static', filename = "image/" + os.listdir(img_dir)[0] )
        return render_template("display_image.html", file=file)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)