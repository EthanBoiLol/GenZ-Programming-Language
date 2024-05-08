import os
import time

ver = "1.0.0"

# What the fuck am I doing with my life?
print("GenZ Compiler v" + ver)
print()
print("Hey there blud, what file should we cook?")

FileName = input("> ")

FileIn = open(FileName, "r")

f = FileIn.read()


# Remove any cheaters that attempts to use c++ syntax normally
f = f.replace(" bool", "")
f = f.replace(" false ", "")
f = f.replace(" true ", "")
f = f.replace(" if(", "")
f = f.replace(" if ", "")
f = f.replace(" return ", "")
f = f.replace(" < ", "")
f = f.replace(" > ", "")
f = f.replace("<=", "")
f = f.replace(">=", "")
f = f.replace(" public ", "")
f = f.replace(" private ", "")
f = f.replace(" else ", "")
f = f.replace(" try ", "")
f = f.replace(" catch ", "")
f = f.replace(" throw", "")
f = f.replace(" std", "")
f = f.replace(" cout", "")
f = f.replace("std::string", "")
f = f.replace("float ", "")
f = f.replace("double ", "")
f = f.replace("int ", "")
f = f.replace("int)", "")
f = f.replace("endl ", "")
f = f.replace(" char ", "")
f = f.replace("cin ", "")
f = f.replace("main( ", "")
f = f.replace("#include", "")
f = f.replace("while", "")
f = f.replace("for ", "")
f = f.replace("for(", "")
f = f.replace("++", "")
f = f.replace("--", "")
f = f.replace("do ", "")
f = f.replace("break;", "")
f = f.replace("continue;", "")
f = f.replace("sizeof(", "")
f = f.replace("struct ", "")
f = f.replace("const ", "")
f = f.replace("& ", "")
f = f.replace("void ", "")
f = f.replace("class ", "")
f = f.replace("protected ", "")
f = f.replace("ofstream ", "")
f = f.replace("ifstream ", "")
f = f.replace("fstream ", "")
f = f.replace(" == ", "")
f = f.replace(" != ", "")
f = f.replace("using namespace ", "")
f = f.replace("min(", "")
f = f.replace("max(", "")
f = f.replace("<iostream>", "")




# After the previous replacement is done, then Replace All GenZ slangs with their c++ equivalents

f = f.replace(" fax ", " bool ") 
f = f.replace(" cap ", " false ") 
f = f.replace(" noCap ", " true ") 
f = f.replace("vibe_check(", " if(") 
f = f.replace(" its_giving ", " return ") 
f = f.replace(" ratios ", " > ") 
f = f.replace(" ratios_+_L ", " >= ") 
f = f.replace(" unratios ", " < ") 
f = f.replace(" unratios_+_L ", " <= ") 
f = f.replace(" highkey ", " public ") 
f = f.replace(" lowkey ", " private ") 
f = f.replace(" big_yikes", " else") 
f = f.replace(" fuck_around", " try") 
f = f.replace(" find_out", " catch") 
f = f.replace(" yeet", " throw") 
f = f.replace(" Shoutout", " std") 
f = f.replace("SpillTea ", "cout ") 
f = f.replace("yap ", "std::string ") 
f = f.replace("period ", " float ") 
f = f.replace("body_count ", " double ") 
f = f.replace("basic ", "int ") 
f = f.replace("slay", "endl") 
f = f.replace("jit ", " char ") 
f = f.replace("rent-free ", " cin ")
f = f.replace(" main_character(", " main(") 
f = f.replace("#fit", "#include") 
f = f.replace("moots", "while") 
f = f.replace("fanum_tax", "for") 
f = f.replace(" extra", "++") 
f = f.replace(" ded", "--") 
f = f.replace(" mew", " do") 
f = f.replace("ick;", " break;") 
f = f.replace("ghost;", " continue;") 
f = f.replace("bde(", "sizeof(") 
f = f.replace("bussy", "struct") 
f = f.replace("glaze ", "const ") 
f = f.replace("bussin ", "&") 
f = f.replace(" flex ", "* ") 
f = f.replace("gagged ", "void ") 
f = f.replace("skibidi ", "class ") 
f = f.replace("gatekeep ", "protected ") 
f = f.replace("ohio ", "ofstream ") 
f = f.replace("florida", "ifstream ") 
f = f.replace("sus ", "fstream ") 
f = f.replace(" mid ", " == ") 
f = f.replace(" cooked ", " != ") 
f = f.replace("cook ", " using namespace ") 
f = f.replace("beta(", "min(") 
f = f.replace("alpha(", "max(") 
f = f.replace("<sigma>", "<iostream>") 


# Oh boy, shitty hack here!
f = f.replace(" cap;", " false;")
f = f.replace(" cap)", " false)")
f = f.replace(" noCap;", " true;")
f = f.replace("basic)", " int)")
#f = f.replace(" sigma;", " iostream;")


## -- write file -- ##
FileOut = open("tmp.cpp", "w")

FileOut.write(f)
FileOut.close()

# Compile C++

time.sleep(1)

buildName = input("Name for the compiled program? ")

os.system("g++ tmp.cpp -o Build/" + buildName)
