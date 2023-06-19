const indexedDB =
    window.indexedDB ||
    window.mozIndexedDB ||
    window.webkitIndexedDB ||
    window.msIndexedDB ||
    window.shimIndexedDB;

    // Open (or create) the database
    const request = indexedDB.open("StrCodeDatabase", 1);

    request.onerror = function (event) {
        console.error("An error occurred with IndexedDB");
        console.error(event);
    };

    // Create the schema on create and version upgrade
    request.onupgradeneeded = function () {
        const db = request.result;
        const store = db.createObjectStore("strCode", { keyPath: "id" });
        store.createIndex("strCode_name", ["name"], { unique: false });
        store.createIndex("name_and_value", ["name", "value"], {
            unique: false,
        });
    };

    request.onsuccess = function () {
        console.log("Database opened successfully");

        const db = request.result;
        const transaction = db.transaction("strCode", "readwrite");     // empieza transaccion (falla si alguna conexion falla)

        const store = transaction.objectStore("strCode");
        


        // Query the data
        const idQuery1 = store.get(1);       //recupera el codigo con los inputs de HTML //en total tenemos 3 datos a recuperar //tiene que conectarse en el mismo puerto
        

        idQuery1.onsuccess = function () {
            console.log("idQuery1", idQuery1.result);
            let strIDB = idQuery1.result.value;
            console.log("String", strIDB);
            if (typeof window === 'object') {
                // It's a browser!
                console.log("It's a browser")
                window.jsGlobalStrCodeHTML = strIDB;
            } else if (typeof global === 'object') {
                // It's a server!
                console.log("It's a server")
                global.jsGlobalStrCodeHTML = strIDB;
            } else {
                // Error
                console.log("Error")
            }
        };

        const idQuery2 = store.get(2);       //recupera el codigo con las keys para transformar
        

        idQuery2.onsuccess = function () {
            console.log("idQuery2", idQuery2.result);
            let strIDB = idQuery2.result.value;
            console.log("String", strIDB);
            if (typeof window === 'object') {
                // It's a browser!
                console.log("It's a browser")
                window.jsGlobalStrCodeRecovery = strIDB;
            } else if (typeof global === 'object') {
                // It's a server!
                console.log("It's a server")
                global.jsGlobalStrCodeRecovery = strIDB;
            } else {
                // Error
                console.log("Error")
            }
        };


        const idQuery3 = store.get(3);       //recupera las palabras clave y sus datos asociados 
        

        idQuery3.onsuccess = function () {
            console.log("idQuery3", idQuery3.result);
            let listIDB = idQuery3.result.value;
            let strIDB = JSON.stringify(listIDB);
            console.log("String", strIDB);
            if (typeof window === 'object') {
                // It's a browser!
                console.log("It's a browser")
                window.jsGlobalStringKeys = strIDB;
            } else if (typeof global === 'object') {
                // It's a server!
                console.log("It's a server")
                global.jsGlobalStringKeys = strIDB;
            } else {
                // Error
                console.log("Error")
            }
        };


        transaction.oncomplete = function () {
            db.close();
        };
    };