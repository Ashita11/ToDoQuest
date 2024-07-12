function fun(idl,uid) {
    obj = new XMLHttpRequest();
    obj.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('id1').innerHTML = this.responseText;
        }
    };
    obj.open('GET', 'display?idl=' + idl + '&uid=' + uid, true);
    obj.send();
}

function fun1(idl,uid) {
    obj = new XMLHttpRequest();
    obj.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('id1').innerHTML = this.responseText;
        }
    };
    obj.open('GET', 'completed?idl=' + idl + "&uid=" + uid, true);
    obj.send();
}

function del(id,uid,nm) {
    obj = new XMLHttpRequest();
    obj.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('id1').innerHTML = this.responseText;
        }
    };
    obj.open('GET', 'delTask?id=' + id + "&uid=" + uid + "&nm=" + nm, true);
    obj.send();
}

function com1(id,uid,nm) {
    obj = new XMLHttpRequest();
    obj.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('id1').innerHTML = this.responseText;
        }
    };
    obj.open('GET', 'delTaskC?id=' + id + "&uid=" + uid + "&nm=" + nm, true);
    obj.send();
}

function com(id,uid,nm) {
    obj = new XMLHttpRequest();
    obj.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('id1').innerHTML = this.responseText;
        }
    };
    obj.open('GET', 'complete?id=' + id + "&uid=" + uid + "&nm=" + nm, true);
    obj.send();
}

function detail(id,uid) {
    obj = new XMLHttpRequest();
    obj.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('dd').innerHTML = this.responseText;
        }
    };
    obj.open('GET', 'details?id=' + id + "&uid=" + uid, true);
    obj.send();
}

document.addEventListener('DOMContentLoaded', (event) => {
    let links = document.getElementsByClassName('a');

    Array.from(links).forEach(function (link) {
        link.addEventListener('click', function (e) {
            Array.from(links).forEach(function (link) {
                link.classList.remove('active');
            });

            this.classList.add('active');
        });
    });

    document.getElementById('textarea').addEventListener('click', function () {
        document.getElementById('popup').style.display = 'block';
    });
});



function closeForm() {
    document.getElementById('popup').style.display = 'none';
}
