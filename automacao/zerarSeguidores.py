import pyautogui as pag
from time import sleep

#sleep(2)
#rint(pag.position())

def cancelarSeguindo():
  # pegar o ultimo seguindo
  topoSeguindo = [877, 244]
  # clicar para deseguir
  pag.click(877, 244, duration=1)
  # comfirmar
  pag.click(704, 355, duration=1)
  proximoSeguindo()


def proximoSeguindo():
  pag.moveTo(971, 272, 1)
  pag.scroll(-80)
  cancelarSeguindo()

cancelarSeguindo()
proximoSeguindo()
cancelarSeguindo()