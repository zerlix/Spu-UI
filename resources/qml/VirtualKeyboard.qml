// VirtualKeyboard.qml
import QtQuick 2.15
import QtQuick.VirtualKeyboard 2.15

Item {
    width: 800 // Setzen Sie einen geeigneten Wert
    height: 250 // Setzen Sie einen geeigneten Wert

    Component.onCompleted: {
        // Setzen Sie die Input-Method-Hints direkt auf der Wurzelkomponente
        inputMethodHints: Qt.ImQueryInput
    }

    InputPanel {
        id: inputPanel
        visible: true
        width: parent ? parent.width : 0
        height: parent ? parent.height : 0

        property var onKeyClick: function(key) {
            console.log("Key clicked:", key);
            keyboard.activeFocusItem = main_window.textEdit;
        }
    }
}
