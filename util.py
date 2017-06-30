def get_function_at(bv, addr):
    blocks = bv.get_basic_blocks_at(addr)
    return blocks[0].function if blocks is not None else None

def find_in_IL(il, addr):
    out = []
    for block in il:
        for i in block:
            if i.address == addr:
                out.append(i)
    return out

def inst_in_func(func, addr):
    out = None
    for block in func:
        for i in block.disassembly_text:
            if i.address == addr:
                out = i
    return out

def dereference_symbols(bv, il_instruction):
    if il_instruction is not None:
        out = []
        for item in il_instruction.tokens:
            try:
                addr = int(str(item), 16)
                func = bv.get_function_at(addr)
                if func is not None:
                    out.append(func.name)
                    continue
            except ValueError:
                pass
            out.append(item)
        il_instruction.deref_tokens = out
    return il_instruction