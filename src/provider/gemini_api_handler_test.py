from .gemini_api_handler import GeminiApiHandler

def test_shorten_with_gemini():
  gemini_api_handler = GeminiApiHandler()
  text = """
    Era uma vez uma doce menina chamada Chapeuzinho Vermelho, que sempre usava uma capa vermelha feita por sua avó. Um dia, sua mãe pediu que ela levasse uma cesta de guloseimas para a avó, que morava sozinha em uma casinha no meio da floresta.

    — Não se desvie do caminho, Chapeuzinho — advertiu sua mãe. — A floresta pode ser perigosa.

    Chapeuzinho Vermelho prometeu que seguiria o caminho e partiu alegremente. Enquanto caminhava, ela admirava as flores e ouvia o canto dos pássaros. Mas, distraída pela beleza da floresta, acabou se afastando do caminho.

    Nesse momento, um lobo astuto a avistou. Ele se aproximou, tentando parecer amigável.

    — Olá, Chapeuzinho Vermelho! — disse o lobo. — Para onde você vai tão apressada?

    — Estou indo visitar minha avó, que está doente — respondeu a menina, sem perceber o perigo.

    O lobo, então, teve uma ideia maligna. Ele sugeriu que Chapeuzinho colhesse algumas flores para alegrar a avó. Enquanto ela se distraía, o lobo correu rapidamente até a casa da avó.

    Ao chegar lá, o lobo bateu na porta.

    — Quem é? — perguntou a avó, com a voz fraca.

    — Sou eu, Chapeuzinho Vermelho! — respondeu o lobo, imitando a voz da menina.

    A avó, sem desconfiar, abriu a porta. O lobo a trancou no armário e se disfarçou com suas roupas, deitando-se na cama.

    Quando Chapeuzinho Vermelho finalmente chegou, ela estranhou a porta aberta, mas entrou assim mesmo.

    — Vovó, estou aqui! — chamou ela.

    — Entre, minha querida! — respondeu o lobo, tentando soar doce.

    Chapeuzinho se aproximou da cama e, ao olhar para a "vovó", notou algo estranho.

    — Vovó, por que você está com olhos tão grandes? — perguntou.

    — Para te ver melhor, minha querida! — respondeu o lobo.

    — E por que você tem orelhas tão grandes? — continuou Chapeuzinho.

    — Para te ouvir melhor! — disse o lobo, já impaciente.

    — E por que você tem dentes tão grandes? — questionou a menina, agora assustada.

    — Para te comer melhor! — rugiu o lobo, pulando da cama.

    Chapeuzinho Vermelho gritou e correu em direção à porta, mas o lobo a alcançou. No entanto, um caçador que passava pela floresta ouviu os gritos da menina e correu para a casa.

    Ele entrou rapidamente e, ao ver o lobo, não hesitou. Com um golpe certeiro, ele salvou Chapeuzinho Vermelho e sua avó, que saiu do armário assustada, mas ilesa.

    O lobo, percebendo que havia sido derrotado, fugiu para a floresta e nunca mais foi visto.

    Chapeuzinho Vermelho e sua avó agradeceram ao caçador e, a partir daquele dia, a menina aprendeu a importância de seguir o caminho e não se distrair com as armadilhas da floresta.

    E assim, Chapeuzinho Vermelho e sua avó viveram felizes e seguras, sempre lembrando da aventura que tiveram.
  """

  shortened_text = gemini_api_handler.shorten_with_gemini(text)

  assert shortened_text is not None
  assert "Little Red Riding Hood" in shortened_text