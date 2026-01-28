Telegram.WebApp.ready()
Telegram.WebApp.expand()

Telegram.WebApp.MainButton.setText("VALIDER COMMANDE")
Telegram.WebApp.MainButton.show()

Telegram.WebApp.MainButton.onClick(() => {
  Telegram.WebApp.sendData(
    JSON.stringify({
      test: "OK"
    })
  )
})
