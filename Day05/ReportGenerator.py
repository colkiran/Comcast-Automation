import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="report.log",
    filemode="a",
    level=logging.INFO
)

def GenRep(flname, retVal):
    gender = {}
    desig = []
    dept = []
    salary = 0
    try:
        FL = open(flname, "r")


        for line in FL.readlines():
            gen = line.split(",")[2]
            des = line.split(",")[3]
            dep = line.split(",")[4]
            if gen not in gender:
                gender[gen] = 1
            else:
                gender[gen] += 1
            if des not in desig:
                desig.append(des)
            if dep not in dept:
                dept.append(dep)
            salary += int(line.split(",")[5])
    except FileNotFoundError as f:
        logging.critical(f)
    else:
        if retVal == "gender":
            for k, v in gender.items():
                logging.info(f"{k} => {v}")
        elif retVal == "desig":
            logging.info(desig)
        elif retVal == "dept":
            logging.info(dept)
        elif retVal == "salary":
            logging.info(salary)
        else:
            for k, v in gender.items():
                logging.info(f"{k} => {v}")
            logging.info(desig)
            logging.info(dept)
            logging.info(salary)
