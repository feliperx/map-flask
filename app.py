from flask import Flask, render_template
import folium

app = Flask(__name__)


# function -> homepage
@app.route('/')  # decorator route to fucntion homepage
def homepage():
    return render_template('homepage.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/users/<username>')
def users(username):
    return render_template('users.html', username=username)


@app.route('/mapView')
def mapView():

    map = folium.Map(
        location=[2.821387, -60.672743], zoom_start=13
    )


    folium.Marker(
        location=[2.5487715,-60.7818621],
        popup="Pedra da Lua",
        icon=folium.Icon(color="green", icon="info-sign"),
    ).add_to(map)
    
    folium.Marker(
        location=[2.808022, -60.671174],
        popup="Ladeira do Beiral",
        icon=folium.Icon(color="orange", icon="flag"),
    ).add_to(map)

    folium.Marker(
        location=[2.822471, -60.664798],
        popup="<b>Ladeira da Praca da Bandeira</b>",
        icon=folium.Icon(color="orange", icon="flag"),
    ).add_to(map)

    folium.Marker(
        location=[2.840178, -60.651140],
        popup="Ladeira da Getulio Vargas",
        icon=folium.Icon(color="orange", icon="flag"),
    ).add_to(map)

    folium.Marker(
        location=[2.849588, -60.642830],
        popup="Ladeira da Cathedral",
        icon=folium.Icon(color="orange", icon="flag"),
    ).add_to(map)

    folium.Marker(
        location=[2.864260, -60.771365],
        popup="Ladeira da TT",
        icon=folium.Icon(color="orange", icon="flag"),
    ).add_to(map)

    

    return map._repr_html_()


# start website
if __name__ == '__main__':
    app.run(debug=True)

# kill service:
# sudo netstat -tulnp | grep :5000
# sudo kill <numberservice>
