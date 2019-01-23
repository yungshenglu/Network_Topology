package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func exec_command(program string, args ...string) {
	cmd := exec.Command(program, args...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()

	if err != nil {
		fmt.Printf("%v\n", err)
	}
}

func main() {
	// Args
	//starter := flag.String("image", "user", "The creation process will start from this user, and add tag behind this value.")
	//starterPort := flag.Int("port", 9487, "The port used by current creation, will be used by a ssh service. And will increase by 1 after a creation process is finished.")
	totalNum := flag.Int("num", 3, "The number of the ssh service we will create.")
	dryRun := flag.Bool("r", false, "Run the command, default is `false`, you need to using -r to specify.")
	clean := flag.Bool("c", false, "Clean all the existed container, default is `false`, using `-c` to specify.")

	flag.Parse()

	if *clean {
		exec_command("./main.sh", "cleanall")
		os.Exit(1)
	}

	data, err := ioutil.ReadFile("./list.txt")
	check(err)
	str := string(data)
	var ports []string
	var containers []string
	for i := 0; i < len(data); i += 8 {
		if str[i] != 10 {
			container := str[i : i+7]
			port := str[i+2 : i+7]
			containers = append(containers, container)
			ports = append(ports, port)
		}
	}

	for i := 0; i < *totalNum; i++ {
		fmt.Println("Current image name: ", containers[i])
		fmt.Println("Current specified port: ", ports[i])
		if *dryRun {
			// run execute command
			exec_command("./main.sh", "build", containers[i], ports[i])
		}
	}

	if *dryRun == false {
		fmt.Println("Running command in Dry-Run mode, do nothing :D, please using -h to check the support of this program!")
	}
}
