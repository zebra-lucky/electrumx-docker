

class ZcashTestnet(EquihashMixin, Coin):
    NAME = "Zcash"
    SHORTNAME = "TAZ"
    NET = "testnet"
    P2PKH_VERBYTE = bytes.fromhex("1D25")
    P2SH_VERBYTES = [bytes.fromhex("1CBA")]
    WIF_BYTE = bytes.fromhex("EF")
    GENESIS_HASH = ('05a60a92d99d85997cce3b87616c089f'
                    '6124d7342af37106edc76126334a2c38')
    DESERIALIZER = lib_tx.DeserializerZcash
    TX_COUNT = 329196
    TX_COUNT_HEIGHT = 68379
    TX_PER_BLOCK = 5
    RPC_PORT = 18232
    REORG_LIMIT = 800
