import galois
import numpy as np

def hex_string_to_coeffs(hex_string, is_lsb_first=True):
    """
    Convert hex string to coefficient list
    
    Parameters:
    hex_string: hex string (with or without '0x' prefix)
    is_lsb_first: True if hex represents coefficients LSB-first, False if MSB-first
    
    Returns:
    List of coefficients in standard format [x^0, x^1, x^2, ...]
    """
    # Remove '0x' prefix if present
    if hex_string.lower().startswith('0x'):
        hex_string = hex_string[2:]
    
    # Convert hex to integer
    value = int(hex_string, 16)
    
    # Convert to binary string
    binary_str = bin(value)[2:]  # Remove '0b' prefix
    
    # Convert to coefficient list
    coeffs = [int(bit) for bit in binary_str]
    
    if is_lsb_first:
        # Input is LSB-first: reverse to get [x^0, x^1, x^2, ...]
        coeffs = coeffs[::-1]
    # If MSB-first: already in [x^(n-1), ..., x^1, x^0] format, need to reverse
    
    return coeffs

def coeffs_to_hex_string(coeffs, output_lsb_first=True):
    """
    Convert coefficient list to hex string
    
    Parameters:
    coeffs: coefficient list [x^0, x^1, x^2, ...]
    output_lsb_first: True to output LSB-first hex, False for MSB-first
    
    Returns:
    Hex string
    """
    if output_lsb_first:
        # LSB hex: [x^0, x^1, x^2, ...] -> binary string x^0 x^1 x^2 ...
        binary_str = ''.join(str(bit) for bit in coeffs)
    else:
        # MSB hex: [x^0, x^1, x^2, ...] -> binary string x^(max) x^(max-1) ... x^0
        binary_str = ''.join(str(bit) for bit in coeffs[::-1])
    
    # Convert to hex
    if binary_str and int(binary_str, 2) > 0:
        return hex(int(binary_str, 2))[2:].upper()
    else:
        return '0'

sparse_input = [15904,5321,12892,10857,15213,6250,10772,7056,11779,14366,3104,15425,4948,889,14262,3420,5451,4756,5028,16303,8218,11596,3401,7633,6844,7661,8307,7579,3250,2210,9548,408,16302,4921,12189,17155,2186,13357,15598,12203,1742,5459,3978,4888,7404,10390,1832,7625,6957,17415,3452,4919,8933,13764,9228,14162,3870,909,13150,17373,14188,1316,4812,10877,15008,4152]  # Example sparse indices
conv_sparse = galois.Poly.Degrees(sparse_input, coeffs=[1]*len(sparse_input), field=galois.GF(2))
print(len(sparse_input))
print(f"Sparse polynomial from indices {sparse_input}: {conv_sparse}")

dense_input = hex_string_to_coeffs("0x1b11ede324e9b6358ac995803221d78eb1a20877b453875f43ddf18657e032c39027ca9787739a60a18785bcba31b18603ded830d1cc0bcd762ed14f79324d4f5ea7932b9cfd0fa74e57add798d662203335293214c62a8b7ef3d4615f44111e4e6a189d885a9d9c2cb2e185130c7f6cb65e05e9495525b8ebf67a56f902e8e7ce719b9e06f02d769125868de4d7ac7396740409465dda223cafb90ede4a8e34e7decde678c0fe26c4ed941cef3d550ec571c4459ad1dfe0d393611eef5b4f03d63133cff34401bf51cf2a43158304126214cf4bdb6b5fa0550b785ca333ef53a30f2e421450f454c05a1ead8df1baccbd6e21700060a4ba8d33dba5b1ce99036628d7f32c79c1d3e31a4da4343b92377ec32f04ae24e758d97b53e9b0b81d19bcf2bd946157ee507a71b5ba5d479940610ef4c6c2159e9bd0fb73b784d6a9ce31bbad36d0385d69b5b46f4a46940506d5ce450e146ea74fa54ad3152ffa099fc44cc5e39dca9962b1ed535227652a46e4ea89507961fe13d6dc8a05757b4b61b7cdcd9c3beaa67f1712e223173cd6df53650a4041a52c32d6914476fa26c5152d99dbe478ff75ada25e80fa8a273c223d6985badea8fd363f67b83a66c8d4dac6831ee03103606047b9d2086562b8b6405b73d4885d3dcf083ce8c15c96f2a114744ec1b94b30385e53430660c771950feac264622912bb1af4e3692399f1b3a5f949aeff9c664a1f39bd1faebbfb0a8278af29680d1c67340607042f7de95e41174ca502f9eb1269ff6fc6a50fc52043f4f9e98ace16bca62765877c9d29cd2b34bb4733148b7b204ef5076f712f2b61ca41bdbb7114cb5a07bdfec7be8bde62f34e0e39424d1cdc225cddb67e4feba711b7895bb1c861930776ce4f5e879cba516364025052f7debc4f667d3e609fc525bb819b8ab45825e07e24985c08e40a0fbc8b84c9c5e2f462e10fef35ed4faa80cb5ade6b9c1d5f0cbde1cd84606135d217702c5ad5d3232d140b5dbdc39d03904779384b66d404319dc313e1deb9fc0278263d43c04faa9cf71dd08cf219fc3cf55aae213fb1a90d86c6c0f49f1cfd2be74d9590f9a88d592dcddc5893b9df47e8324f9a12d69525b9810949be53e121b11a7d1b6dbe655770a6b28fcfb3bc3907473b129f71b7db3bda0e95920fa09d18c758980293c861263be289270a3944a42bc8fb86af9445110134f478e525ebfabee8c32b52e9860c017128ffbd725e1421db045d8b9e9e08ac9e9c356357c5077c151af6ec07fd132b77f38012478c235ee4d93994f48925d5d3a41321a5c88c2d1ed995dd469ac660cc4b273a0ed472a66a57fc771e244d9d73e50cd44846977e62be785145df0845f0c0da27b9540f60c296ac3a449ed18ec64f00c44929d9f92834d7527ee1743bbc784deb24fa922886deaa28cf20ea2f599877b76e3e8308d2ea0e31ecaa175e7e01918e59ad2f2be8160ffcc5c189b0f9ed5d0a2b910d7aee1693297526c441af060897be57525d950dc012c0b63ff318e393d8743f29d96f161f7f99bf6ab69647e3058a02ee4ef1916b13b758c9d42b135db4e32b69f63ea559f89201bcc151b39f3c894acf2087cc27aa739d3086e279f5acc9918571763d2d33184c9ed93778247dbd457f8eb6bfbf9238a5d1d431385683a15543cf6074bf85740672384dd26e54c0b1efe7dfe316c7b1bd293971777d057db6b5a869c3c39e50518ddf40cbfdc2dc59b41c182a843d40560b653f1b99cdb59dd0dcb80611ff2a3d1df4b01ab013e4fd3f4c8ae38658646253a78c5c7fc4187c5a5cf1bda97d042aab8d387acdfd8e8ea60633ecaf70a4cd6299373c2a3beb42d20fe463a0badebf98d870280c0103c943a6f79bd475d1bef39f43cd2080a98b34d232c0855fe6e6fd3d8922ec7b259794ae681529aec5cd0a6f773ee6c8023b4338e6bedb9c19558703ccb29e2074d85921762856bc7a8d3e1c098635d00f24a807161a7a4a6506ba6c7d5b4602a9d8e00361df04e72481bfae57ba76a61d0c8c4ba5fdc3120995e2ee6b4c8ce7a18d18fe9d2577d128233b011dd0d4e90cab85d02163ef534a9592886f6f5a7bf87fca86c9a658e318f50fd2e57714dbbe132d9175aa21473ec835dcb54692d32e5806e4e51927f0fc7b96f4bd930012369570c659c8d2a114d1b43f9a2b1c3393abc9b549b801cab83f1f70b68b0f4fad11e7e47da70e1479e2db29161a4ea6908376a924fbeb00af94496a8ddc368bccfaeee215093e37a5aa4e77f8e33177aa9505a17a428f54d1133c0d2594b264d859d25021d4850272a49b1806ac568f95bcde224df6cc2aaf2359c537389e6ea9fd7fc09ccaa4d084bcb1aa0264b49e382285963aeb3e9373246587e14e5832f7d2c97ca674d3b52887d4d368b6abbc24342cf80a8580dc8d70190507a2e11efaa106150b9826bebb9a3a9b805fe1421bbc850e2a0d29eda869f3e481df535463d2067a153c72231436e0c44bea13f78dc9f0c2c64d456951fc9d084b48afa90a75531bef133cebde6d7b7a1d91b989fa413c8ae52d6e8d421b5069bfcd6d0e765f93299a64904c77968b9b920e8547f0f6dc16dd45e85d20f348519df965e796b5c2222cb5c600ae5739bbde457880a3e96caef11822cfc106038a168d20ebfcac7ec1c4995e6ec4d2773e7b26308c4e2ebd05e65d4060c91e0e5a0ba941180bac9dbd51c9cf39269a5ce2530d16ff8e98a618e2e823d639232b796fcb5d1d38b9f2ba4f893f0b1ba19d9ba5f7e916eebbecb3761514355ecd2c5d43a9beac33324677e4fc26a114482e4ef583cd7daf56ef59ab5a82276600b8410ec1f7ad46218846005fca8735ab91b1319a5934fd5eff943ac547bed509bcb98647298370b6b450bac29cb88a1f76bab5b5b80f31f23fecc497637dcc394023d122797efb6cd6a239da775222177807627230ec0fd1825742c37475c5d78a4f57a2496347541ecab09764994239b244a794c3ac7fa697815ccf1bdd6c24436898ea7c32814e3f2e8565d6821dbc890039f625f810d2d6a460021021b50bd34a7b275df25dfc2248f34b142e624baa0537d575fbad37daa6d429c1860c71ae65dd9530a162", is_lsb_first=False)

#dense_input =[0,1,0,0,0,1,0,0, 0,1,1,1,0,1,1,1, 0,0,0,0,1,1,1,1, 1,1,1,1,0,0,0,0, 0,1,0,1,0,1,0,1, 1,1,0,0,1,1,0,0, 1,0,1,0,1,0,1,0, 1,1,0,0,1,1,0,0] # Example dense bits
#dense_input = dense_input[::-1]  # Convert to MSB-first for galois
print(f"Dense polynomial from hex : {dense_input}")

GF2 = galois.GF(2)
n = 17669  # Example degree
modulus = galois.Poly([1] + [0]*(n-1) + [1], field=GF2)  # X^n - 1
poly1 = conv_sparse
poly2 = galois.Poly(dense_input, field=GF2)
    
result = (poly1 * poly2) % modulus
# print(f"Result of multiplying sparse {conv_sparse}")
# print(f"with dense {poly2}: ")
print(result)

# 
#print(result.coefficients())
# if len(result.coefficients) > 0:
#     result_coeffs_array = result.coefficients
#     result_coeffs = result_coeffs_array.tolist()
#         # Convert to LSB-first format
#     result_coeffs = result_coeffs[::-1]
# else:
#     result_coeffs = [0]
    
#     # Pad to length n
# result_coeffs = result_coeffs[:n] + [0] * max(0, n - len(result_coeffs))

# print(f"Result coefficients (LSB-first, length {n}): {result_coeffs}")

print(coeffs_to_hex_string(result.coefficients(), output_lsb_first=True))
